import quarterback

def test_qb_name():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.name == "Dan Marino"

def test_qb_team():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.team == "Miami Dolphins"

def test_qb_att():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.att == 8358

def test_qb_cmp():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.cmp == 4967

def test_qb_yds():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.yds == 61361

def test_qb_td():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.td == 420

def test_qb_intc():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.intc == 252

def test_qb_a():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino._Quarterback__a == 1.4714046422589135

def test_qb_b():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino._Quarterback__b == 1.0853972242163197

def test_qb_c():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino._Quarterback__c == 1.0050251256281408

def test_qb_d():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino._Quarterback__d == 1.6212311557788945

#REMOVED TO MATCH README
'''def test_qb_pr():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert round(marino.passer_rating,1) == 86.4'''

def test_string():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    assert marino.__str__() == "Dan Marino plays for the Miami Dolphins"

def test_neg_a():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    marino.cmp = -1000
    assert marino.calc_a() == 0

def test_neg_b():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    marino.yds = -1000
    assert marino.calc_b() == 0

def test_neg_c():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    marino.td = -1000
    assert marino.calc_c() == 0

def test_neg_d():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",8358, 4967, 61361, 420, 252 )
    marino.intc= 1000
    result = marino.calc_d()
    assert result == 0

###TEST GREATER THAN####
def test_greater_a():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",10,8, 61361, 420, 252 )
    assert marino.calc_a() == 2.375

def test_greater_b():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",2, 4967, 30, 420, 252 )
    assert marino.calc_b() == 2.375

def test_greater_c():
    marino = quarterback.Quarterback("Dan Marino", "Miami Dolphins",10, 4967, 61361, 2, 252 )
    assert marino.calc_c() == 2.375