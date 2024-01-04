from google.cloud import translate_v2

class PaymentConfirmationSystem:
    def __init__(self):
        self.translate_client = translate_v2.Client()

    def translate_text(self, text, target_language):
        result = self.translate_client.translate(text, target_language=target_language)
        return result['translatedText']

    def confirm_payment(self, confirmation_message, language):
        translated_message = self.translate_text(confirmation_message, language)
        return translated_message

# Example Usage
payment_system = PaymentConfirmationSystem()

# User confirms payment through text input
confirmation_message_text = "Payment confirmed. Thank you!"
selected_language_text = 'es'  # Replace with the user's selected language code
translated_confirmation_text = payment_system.confirm_payment(confirmation_message_text, selected_language_text)
print("Translated Confirmation (Text):", translated_confirmation_text)

# User confirms payment through voice input
# In a real-world scenario, you would use a Speech-to-Text API for processing voice input
confirmation_message_voice = "Voice input representing payment confirmation"
selected_language_voice = 'fr'  # Replace with the user's selected language code
translated_confirmation_voice = payment_system.confirm_payment(confirmation_message_voice, selected_language_voice)
print("Translated Confirmation (Voice):", translated_confirmation_voice)

# User confirms payment through image input
# In a real-world scenario, you would use Optical Character Recognition (OCR) for processing image input
confirmation_message_image = "Image input representing payment confirmation"
selected_language_image = 'hi'  # Replace with the user's selected language code
translated_confirmation_image = payment_system.confirm_payment(confirmation_message_image, selected_language_image)
print("Translated Confirmation (Image):", translated_confirmation_image)
