import Flask
import jinja2
import requests
import spacy
import nltk

class Chatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self._responses = {
            "What is your name?": "My name is HealsCure.",
            "How are you today?": "I am doing well, thank you for asking. How are you?",
            "I am fine, thank you.": "That is good to hear.",
            "What is the difference between HealsCure and a doctor?": "The main difference between HealsCure and a doctor is that HealsCure is a computer program, while a doctor is a human being. A doctor has years of training and experience, while HealsCure is only as good as the data that it.",
          "What is HealsCure?": "HealsCure is a website that provides a platform for users to get personalized medical diagnosis using the latest AI technology.",
            "How does HealsCure work?": "HealsCure works by collecting information about a user's symptoms and medical history. This information is then used to create a personalized medical diagnosis.",
            "Is HealsCure accurate?": "HealsCure is designed to be as accurate as possible. However, it is important to note that HealsCure is not a substitute for professional medical care. If you have any concerns about your health, you should always consult with a doctor.",
            "How much does HealsCure cost?": "HealsCure is currently free to use. However, there may be fees for certain features in the future.",
            "What are the benefits of using HealsCure?": "The benefits of using HealsCure include:* Convenience: You can get a personalized medical diagnosis from the comfort of your own home.* Speed: You can get a diagnosis in minutes, rather than waiting weeks or months to see a doctor.* Affordability: HealsCure is currently free to use.",
            "What are the drawbacks of using HealsCure?": "The drawbacks of using HealsCure include:* Accuracy: HealsCure is not a substitute for professional medical care. If you have any concerns about your health, you should always consult with a doctor.* Privacy: HealsCure collects personal information about its users. This information is used to provide personalized medical diagnosis, but it could also be used for other purposes.",
            "How can I sign up for HealsCure?": "You can sign up for HealsCure by visiting the HealsCure website and clicking on the Sign Up button. You will then be asked to provide some basic information, such as your name, email address, and date of birth.",
            "How do I use HealsCure?": "Once you have signed up for HealsCure, you can use it to get a personalized medical diagnosis. To do this, you will need to provide HealsCure with some information about your symptoms and medical history. You can then answer a few questions about your symptoms. HealsCure will then use this information to create a personalized medical diagnosis.",
            "What happens if I have a question about HealsCure?": "If you have a question about HealsCure, you can contact the HealsCure support team by visiting the HealsCure website and clicking on the Contact Us button.",
            "What are the risks of using HealsCure?": "The risks of using HealsCure include:* Inaccuracy: HealsCure is not a substitute for professional medical care. If you have any concerns about your health, you should always consult with a doctor.* Privacy: HealsCure collects personal information about its users. This information is used to provide personalized medical diagnosis, but it could also be used for other purposes.* Misdiagnosis: HealsCure is a computer program, and as such, it is not perfect. There is always a risk that HealsCure could misdiagnose a condition.",
            "How can I be sure that HealsCure is accurate?": "HealsCure is designed to be as accurate as possible. However, it is important to note that HealsCure is not a substitute for professional medical care. If you have any concerns about your health, you should always consult with a doctor.",
            "What should I do if I am not satisfied with the diagnosis from HealsCure?": "If you are not satisfied with the diagnosis from HealsCure, you should always consult with a doctor. A doctor can provide you with a more accurate diagnosis and treatment plan.",
        }

    def get_response(self, message):
        if message in self._responses:
            return self._responses[message]
        else:
            doc = self.nlp(message)
            # Extract the entities from the message.
            entities = [ent.text for ent in doc.ents]
            # Extract the keywords from the message.
            keywords = nltk.word_tokenize(message)
            # Generate a response based on the entities and keywords.
            response = "I understand that you are interested in {}. Can you tell me more about that?".format(" ".join(keywords))
            return response

    def handle_message(self, message):
        response = self.get_response(message)
        print(f"User: {message}")
        print(f"Chatbot: {response}")
        return response

app = Flask(__name__)

@app.route("/")
def chatbot():
    return render_template("chatbot.html", chatbot=Chatbot())

if __name__ == "__main__":
    app.run(debug=True)
