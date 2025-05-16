# add necessary imports for your flask app here

# this has been called from flask route /send_message, which by itself is triggered by the user sending a message to the chat box
def get_bot_response(message):
    # In a real application, you might integrate with an AI service here
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm functioning well. How about you?",
        "bye": "Goodbye! Have a great day!",
        "help": "I can answer simple questions. Just type your message in the chat box."
    }

    message = message.lower()

    # Check if the message contains any of our keywords
    for key in responses:
        if key in message:
            return responses[key]

    # Default response
    return "I'm not sure how to respond to that. Can you try asking something else?"


# this has been called from index.html, a JS script in the index.html file
@app.route('/bot')
def bot():
    return render_template('bot-main.html')

# this has been called from bot-main.html, a JS script in the bot-main.html file
@app.route('/send_message', methods=['POST'])
def send_message():
    logger.info('in the bot route - send_message')
    try:
        # Get the message from the form
        user_message = request.form.get('message', '')
        logger.info(f'user_message: {user_message}')
        if not user_message.strip():
            logger.info('Message cannot be empty')
            return "Message cannot be empty", 400

        # Add a small delay to simulate processing (optional)
        time.sleep(1)

        # Get bot response
        logger.info('getting bot response')
        bot_response = get_bot_response(user_message)
        logger.info(f'bot_response: {bot_response}')

        # Return the message template with both user message and bot response


        return render_template('bot-message.html',
                               user_message=user_message,
                               bot_response=bot_response)
    except Exception as e:
        app.logger.error(f"Error processing message: {str(e)}")
        return "An error occurred", 500


if __name__ == '__main__':
    app.logger.info('Starting Flask application')
    app.run(host="0.0.0.0", debug="true", port=9000)
