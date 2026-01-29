

import numpy as np 

def convert_to_floats(rows):
    """convert a list of string tuples to a ndarray of floats"""

    # قائمة فارغة لتخزين النتائج
    result = []
    
    # الـ To-Do: يجب كتابة جملة الـ for هنا لتمري على كل سطر (row)
    for row in rows:
        # تحويل السطر لمصفوفة numpy
        value = np.asarray(row)
        # تحويل نوع البيانات لأرقام عشرية
        value = value.astype(float)
        # إضافة السطر للنتائج
        result.append(value)

    # تحويل القائمة النهائية لمصفوفة numpy كاملة (Matrix)
    return np.array(result)