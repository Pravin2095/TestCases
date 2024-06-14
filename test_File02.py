import pytest


class Test_Cases:                          # Class name must be in Capital latter otherwise it's showed 'Empty Suite'.

    @pytest.mark.Arithmatic
    def test_Addition(self):
        A = 50
        B = 150
        Addition = A + B
        print(Addition)

        if Addition == 200:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Minus(self):
        C = 450
        D = 135
        Minus = C - D
        print(Minus)

        if Minus == 315:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Multi(self):
        A = 25
        B = 12
        Multi = A * B
        print(Multi)

        if Multi == 300:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Division(self):
        A = 150
        B = 3
        Division = A // B
        print(Division)

        if Division == 50:
            assert True         # assert is check condition according to the code otherwise it's give 'Assertion Error'.
        else:
            assert False


    def test_String(self):
        Name = "Pravin Vinayak Ingle"
        print(Name)

        if "Pravin" in Name:
            assert True
        else:
            assert False


    def test_List(self):

        List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        print(List)

        if 11 in List:
            assert True
        else:
            assert False
