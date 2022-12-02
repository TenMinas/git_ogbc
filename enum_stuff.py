
def get_enum(k):
    # BSB Table data paths
    a = {"ip1" : "/home/gary/coding/ogdb/BT_INPUT_DATA/o_bsb_tables.csv"}
    b = {"ip2" : "/home/gary/coding/ogdb/BT_INPUT_DATA/smaller_test_data.csv"} # Clean BSB Table Data
    m = {"bsb_sort_first" : 426177}
    n = {"bsb_sort_last" : 426180}

    # Book / Chapter info / Bible info
    c = {"bc_ip" : "/home/gary/coding/ogdb/BT_INPUT_DATA/BC_Info.csv"} 
    d = {"nt_wpath" : "/home/gary/Documents/GARY_FILES/gbc/GREEK_WORDS"}
    e = {"ot_wpath" : "/home/gary/Documents/GARY_FILES/gbc/HEBREW_WORDS"}

    # Final Bible output
    f = {"bc_op" : "/home/gary/coding/ogdb/BIBLE_CHAPTERS/"} 
    # BP_output_path = "/home/gary/coding/ogdb/BP_2/"

    # Word stuff
    # General path info
    g = {"test_wpath" : "/home/gary/coding/ogdb/word_test"} # Test Version - Path to Words
    h = {"stest_wpath" : "/home/gary/coding/ogdb/small_word_test"} # Small Test Version
    z = {"GW" : "/GREEK_WORDS"}
    j = {"HW" : "/HEBREW_WORDS"}

    p = {"first_g_word" : 1}
    # Actual last Strong's Greek word number
    q = {"last_g_word" : 5624} 
    r = {"first_h_word" : 1}
    # Actual last Strong's Hebrew word number 
    s = {"last_h_word" : 8674} 
    # This is a list of character strings to use as keys in the parsing
    t = {"word_key_list" : ["# Word", "# Gary", "# Transliteration", "# BibleHub Definition & Usage", "# BibleHub Definition", "# Part of Speech", "# NASB Translation", "# Phonetic Spelling", "# Transliteration | Phonetic Spelling", "# Occurrences", "# NASB Word Origin", "# Origin Ref 1", "# Origin Ref 2", "# Origin Ref 3", "# Occurrences Link", "# BibleHub Link", "# Blue Letter Bible Usage – Outline", "# Blue Letter Bible Outline", "# Helps Word Studies", "# Blue Letter Bible – Strong’s Definition", "# Blue Letter Bible Strong’s Definition", "# Blue Letter Bible Vines", "# NET Notes", "# Date", "# Initial Date"]}
    u = {"start_next_key" : "##"}

    # Obsidian reated info
    y = {"b_link" : "b00001"} # Bible book / chapter Obsidian link-to code
    l = {"w_link" : "s00001"} # Strong's word Obsidian link-to code

    data = {**a, **b, **c, **d, **e, **f, **g, **h, **z, **j, **y, **l, **m, **n, **p, **q, **r, **s, **t, **u}

#####################

# data === a packed dict
# k === a key in the data
# v === the value for the requested key

    v = data.get(k)
    return(v)

#####################
# This is used to test the code
print(get_enum("ip1"))