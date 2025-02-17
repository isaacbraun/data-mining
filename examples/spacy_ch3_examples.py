# Custom components are great for adding custom values to documents, tokens and spans, and customizing the `doc.ents`.


import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
# Makes a list using the nlp.pipe method
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns, '\n')

# Create a custom PhraseMatcher based on the nlp.vocab model
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# Define the custom component
@Language.component("animal_component")
def animal_component_function(doc):
    # Apply the matcher to the doc
    matches = matcher(doc)
    
    # Create a Span for each match and assign the label "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    
    # Overwrite the doc.ents with the matched spans
    doc.ents = spans
    return doc


# Add the component to the pipeline after the "ner" component
nlp.add_pipe("animal_component", after="ner")
# last=True
# first=True
# before="ner"
# after="tagger"

print(nlp.pipe_names, '\n')

# Process the text and print the text and label for the doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
