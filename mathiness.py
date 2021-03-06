#!/usr/bin/env python3

import random

print("Hello? I'd like to see what you think about a Lemma I've been working on in my spare time.")

nouns = ["plane", "planar coefficients", "structure", "disphrenials", "altcurve", \
         "discontinuity", "conjecture", "aliter", "transport of structure", "isomorphism", "algebraic system"]

adjectives = ["argand", "Euler", "Eilenberg", "arbitrarily prime", "coprime", "genefinite", \
              "modulo out by", "well-defined", "sufficiently nice"]

adverbs = ["arbitrarily", "by way of contradiction", "without loss of generality"]

verbs = ["fly", "b-transport", "translation"]

clauses = ["the following are equivalent", "it obtains that"]

greekletters = ["α", "β", "ξ", "φ"]

symbols = ["(ei)1 ≤ i ≤ n", "(∅)/(∅)"]

print ("Let " + random.sample(greekletters, 1)[0] + " be any " + random.sample(adjectives, 1)[0] + " "
        + random.sample(nouns, 1)[0] + ".")
print ("Let " + random.sample(symbols, 1)[0] + " be a basis for " + random.sample(adjectives, 1)[0]
        + " " + random.sample(nouns, 1)[0] + " " + random.sample(greekletters, 1)[0] + ".")
print ("There is a " + random.sample(nouns, 1)[0] + " onto the " + random.sample(adjectives, 1)[0]
        + " " + random.sample(nouns, 1)[0] + ", and by "
        + random.sample(verbs, 1)[0] + " of this " + random.sample(nouns, 1)[0]
        + " it obtains that a " + random.sample(nouns, 1)[0] + " is equivalent to "
        + random.sample(nouns, 1)[0] + ".")
