import Add
def test_add():
    assert Add.add(7,3) == 10
    assert Add.add(7) == 9
    assert Add.add(5) == 7
def test_product():
    assert Add.product(5,5) == 25
    assert Add.product(5) == 10
    assert Add.product(7) == 14
    
