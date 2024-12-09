


from irspy import irspy




if __name__ == "__main__":

    parser = irspy("data/202000079349300140_public.xml")

    tree = parser.get_tree()

    print("Done")




