def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство"
    assert category.products == []

    assert category.product_count == 0
    assert category.category_count == 1
