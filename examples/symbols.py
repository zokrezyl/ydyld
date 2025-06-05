from ydyld.session import YdyldSession


def main():
    # first create a sessio
    session = YdyldSession()

    for image in session.get_images():
        print(f"Image: {image.name}, Index: {image.index}")
        for symbol in image.symbols():
            print(
                f"  Symbol: {symbol.name}, Address: {symbol.address:#x}, Kind: {symbol.kind}"
            )


if __name__ == "__main__":
    pass
    main()
