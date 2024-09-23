import spacy

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extract entities from the provided text.
    This can be used to identify food preferences, allergies, etc.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
if __name__ == "__main__":
    text = "I am allergic to peanuts and I love running."
    entities = extract_entities(text)
    print(entities)
