# Import and set up txtai translation model.
from txtai.pipeline import Translation

translate = Translation()

# Languages only available in txtai
start = time()

print(translate("father", "ast"))
print(translate("father", "ba"))
print(translate("father", "br"))
print(translate("father", "ff"))
print(translate("father", "ilo"))
print(translate("father", "lg"))
print(translate("father", "ln"))
print(translate("father", "oc"))
print(translate("father", "ss"))
print(translate("father", "tn"))
print(translate("father", "wo"))

print(f"{time()-start} seconds to finish")