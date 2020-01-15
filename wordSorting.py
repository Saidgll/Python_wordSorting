keyWord = "wheather is so good in today"

words = keyWord.split()

words.sort()

print(words)

for wordy in words:
    print(wordy)


print("*****************************")
print("Your Turn")
print("*****************************")

keyWordOne = str(input("You should write a few words. Let's   : "))

yourWords = keyWordOne.split()

for wordyOne in keyWordOne:
    print(wordyOne)