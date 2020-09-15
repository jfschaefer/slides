abstract Math = {
    cat Object; Property; Statement;
    fun
        group : Object;
        abelian : Property;
        commutative : Property;
        addProperty : Property -> Object -> Object;
        hasProperty : Object -> Property -> Statement;
}
