def sardinify_text(input_text: str) -> str:
    """
    Convert every token that starts with an s to 'sardine' (preserving case).
    :param input_text: The string which is to be 'sardinified'
    :return: The text where ever word that corresponds to a word starting
        with 's' in the original input has been converted to 'sardine'.
    """
    words = input_text.split(" ")
    new_words = []
    for word in words:
        if not len(word):
            new_words.append(word)
        elif word[0] == 's':
            new_words.append("sardine\n" if word[-1] == '\n' else "sardine" )
        elif word[0] == 'S':
            new_words.append("Sardine\n" if word[-1] == '\n' else "sardine" )
        else:
            new_words.append(word)
    return " ".join(new_words)


if __name__ == "__main__":

    lyrics = """
    You're better than the best
    I'm lucky just to linger in your light
    Cooler then the flip side of my pillow, that's right
    Completely unaware
    Nothing can compare to where you send me,
    Lets me know that it's OK, yeah it's OK
    And the moments where my good times start to fade
    You make me smile like the sun
    Fall out of bed, sing like a bird
    Dizzy in my head, spin like a record
    Crazy on a Sunday night
    You make me dance like a fool
    Forget how to breathe
    Shine like gold, buzz like a bee
    Just the thought of you can drive me wild
    Oh, you make me smile
    Even when you're gone
    Somehow you come along
    Just like a flower poking through the sidewalk crack and just like that
    You steal away the rain and just like that
    You make me smile like the sun
    Fall out of bed, sing like a bird
    Dizzy in my head, spin like a record
    Crazy on a Sunday night
    You make me dance like a fool
    Forget how to breathe
    Shine like gold, buzz like a bee
    Just the thought of you can drive me wild
    Oh, you make me smile
    Don't know how I lived without you
    Cause every time that I get around ya
    I see the best of me inside your eyes
    You make me smile
    You make me dance like a fool
    Forget how to breathe
    Shine like gold, buzz like a bee
    Just the thought of you can drive me wild
    You make me smile like the sun
    Fall out of bed, sing like a bird
    Dizzy in my head, spin like a record
    Crazy on a Sunday night
    You make me dance like a fool
    Forget how to breathe
    Shine like gold, buzz like a bee
    Just the thought of you can drive me wild
    Oh, you make me smile
    Oh, you make me smile
    Oh, you make me smile
    """
    
    output_text = sardinify_text(lyrics)
    print(output_text)