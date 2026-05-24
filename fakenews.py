import random as rd

def generate_fake_news():
    subjects = ["The government", "Scientists", "Celebrities", "Aliens", "Time travelers"]
    verbs = ["have discovered", "are hiding", "are planning", "have invented", "are controlling"]
    objects = ["a new energy source", "the secret to immortality", "a conspiracy theory", "a new planet", "the meaning of life"]

    subject = rd.choice(subjects)
    verb = rd.choice(verbs)
    obj = rd.choice(objects)

    fake_news = f"{subject} {verb} {obj}."
    return fake_news    


if __name__ == "__main__":
    print(generate_fake_news())
