import main
import quarterback

brady = main.brady
montana = main.montana

def test_brady_name():
    assert brady.name == "Tom Brady"

def test_brady_team():
    assert brady.team == "New England Patriots"

def test_brady_a():
    assert brady._Quarterback__a == 1.71701244813278

def test_brady_b():
    assert brady._Quarterback__b == 1.1009128630705394

def test_brady_c():
    assert brady._Quarterback__c == 1.0771784232365145

def test_brady_d():
    assert brady._Quarterback__d == 1.9351659751037344

def test_brady_pr():
    assert main.brady_pr == 97.2

def test_brady_string():
    assert brady.__str__() == "Tom Brady plays for the New England Patriots"

def test_montana_name():
    assert montana.name == "Joe Montana"

def test_montana_team():
    assert montana.team == "San Francisco 49ers"

def test_montana_a():
    assert montana._Quarterback__a == 0

def test_montana_b():
    assert montana._Quarterback__b == 1.1304952698942683

def test_montana_c():
    assert montana._Quarterback__c == 1.0127991096271565

def test_montana_d():
    assert montana._Quarterback__d == 1.7304071600816175

def test_montana_pr():
    assert main.montana_pr == 64.6

def test_montana_string():
    assert montana.__str__() == "Joe Montana plays for the San Francisco 49ers"

def test_comp():
    result = brady < montana
    assert result == "Tom Brady is a better quarterback than Joe Montana"

def test_brady_isinst():
    assert isinstance(brady, quarterback.Quarterback)

def test_montana_isinst():
    assert isinstance(montana, quarterback.Quarterback)