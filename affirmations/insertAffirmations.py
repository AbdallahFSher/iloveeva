from .models import Affirmation

def insert_affirmations(affirmations_file):

    with open(affirmations_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            affirmation_text = line.strip()
            if affirmation_text:
                a = Affirmation(text=affirmation_text)
                a.save()