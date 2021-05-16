# Модуль для расчета результатов

# Здесь должен быть твой код
def index_ryf(x1, x2, x3):
    a = (4 * (x1 + x2 + x3) - 200) / 10
    return a
def test_ryf(v, a):
    if (v >= 15 and a >= 15) or (13 <= v <= 14 and a >= 15.5) or (11 <= v <= 12 and a >= 18) or (9 <= v <= 10 and a >= 19.5) or (7 <= v <= 8 and a >= 21):
        return("Низкий, срочно обратитесь к врачу!")
    if (v >= 15 and 11 <= a < 15) or (13 <= v <= 14 and 12.5 <= a < 16.5) or (11 <= v <= 12 and 14 <= a < 18) or (9 <= v <= 10 and 15.5 <= a < 19.5) or (7 <= v <= 8 and 17 <= a < 21):
        return("Удовлетворительный, обратитесь к врачу!")
    if (v >= 15 and 6 <= a < 11) or (13 <= v <= 14 and 7.5 <= a < 12.5) or (11 <= v <= 12 and 9 <= a < 14) or (9 <= v <= 10 and 10.5 <= a < 15.5) or (7 <= v <= 8 and 12 <= a < 17):
        return("Средний, возможно, стоит дополнительно обследоваться у врача.")
    if (v >= 15 and 0.5 <= a < 6) or (13 <= v <= 14 and 2 <= a < 7.5) or (11 <= v <= 12 and 3.5 <= a < 9) or (9 <= v <= 10 and 5 <= a < 10.5) or (7 <= v <= 8 and 6.5 <= a < 12):
        return("Выше среднего.")
    if (v > 15 and a < 0.5) or (13 <= v <= 14 and  a < 2) or (11 <= v <= 12 and a < 3.5) or (9 <= v <= 10 and a < 5) or (7 <= v <= 8 and a < 6.5):
        return("Высокий.")
    