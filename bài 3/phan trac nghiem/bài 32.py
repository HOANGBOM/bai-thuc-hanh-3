def my_function ( y ) :
    var = 1
    while ( y > 1) :
        var *= y
        y -= 1
    return var
assert my_function (8) == 40320
print ( my_function (4) )
# đáp án : câu c