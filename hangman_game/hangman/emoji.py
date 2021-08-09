def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":D": "😃",
        ":(": "😞",
        ":)": "😌",
        ":|": "😵",
        ":;": "😬",
        ":w": "👋",
        ":h": "🎉🎊"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    print(output)
