# Strings
text = "X-DSPAM-Confidence:    0.8475";

x = text.find(" ")
y = text[x:]
fy=float(y)
print(fy)
