import random
import sentry_sdk
sentry_sdk.init("https://8e577dc11e2743b4bb2581da3bbcc5a9@sentry.io/1307203")
def answer(question):
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    random.seed(question)
    return random.choice(answers)


if __name__ == "__main__":
    print(answer(input("QUESTION: ")))
