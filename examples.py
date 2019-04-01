from flashtext.keyword import *

if __name__ == "__main__":

    kp = KeywordProcessor()

    kp.add_keyword("A B", "@[X Y]", kp_name="1st")
    kp.add_keyword("A B", "@[X Y]", kp_name="2nd")

    s = "A B"
    r = kp.extract_keywords(s, kp_name="1st")
    print(r)

    r = kp.extract_keywords(s, kp_name="2nd")
    print(r)

    import pprint as pp

    pp.pprint(kp.keyword_trie_dict, indent=2)
