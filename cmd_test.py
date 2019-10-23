import ciar

class cmd_test(ciar.ciar_module):
    confstring_def = """
    cmd_test(
    param0,
    param1="2",
    param2="C1|C2a,C2b|C3",
    param3="cmd_serial(param1="3")
    )
    """

if __name__ == "__main__":
    c = cmd_test()
    c.check()
