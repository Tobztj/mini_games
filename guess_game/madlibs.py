name = input("What is your name? ")

adj1 = input('Adjective... ')
noun = input('Noun... ')
verb = input('Verb...  ')
adverb = input('Adverb.. ')
adj2 = input("Adjective..  ")
noun2 = input('Noun.. ')
noun3 = input('Noun')


madlib = f"Today I went to the zoo. I saw a(n)\n" \
         f"{adj1} \n" \
         f"{noun} jumping up and down in its tree. \n" \
         f"He {verb} {adverb} \n" \
         f"through the large tunnel that led to its {adj2} \n" \
         f"{noun2}. I got some peanuts and passed \n" \
         f"them through the cage to a gigantic gray {noun3} \n" \
         f"towering above my head."

print(madlib)