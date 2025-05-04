from textnode import TextType, TextNode

def main():
    test = TextNode("test text", TextType.Normal, "https://try.this")
    print(test)

main()