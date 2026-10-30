# 1. Görev listesine görev ekle ve task listesini geri dön(bu işlem için metotlarda nasıl değer dönülür incelemen gerekebilir.) (return keyword araştır)
def add_task(task_list: list, task: str) -> list:
    task_list.append(task)
    return task_list
    pass

# 2. Görev listesinde bir görevi sil ve task listesini geri dön(bu işlem için metotlarda nasıl değer dönülür incelemen gerekbilir)
def remove_task(task_list: list, task: str) -> list:
    task_list.remove(task)
    return task_list
    pass

# 3. Uzunluğu 10 karakterden fazla olan görevleri filtrele ve bu görevleri geri dön.
def filter_long_tasks(task_list: list) -> list:
    filtered_tasks=[]
    for task in task_list:
        if len(task)>10:
            filtered_tasks.append(task)
    return filtered_tasks                             
    pass

# 4. Görev sayısı çift mi kontrol et ve bu değeri geri dön
def is_even_task_count(task_list: list) -> bool:
    gorev_sayisi=len(task_list)
    if gorev_sayisi%2==0:
        return True
    else:
        return False
    pass

# 5. Görev listesindeki tüm görevleri büyük harfe çevir
def uppercase_tasks(task_list: list) -> list:
    for task in task_list:
        task.upper()
    pass

# 6. Görev listesindeki görevleri ters sırala
def reverse_tasks(task_list: list) -> list:
    task_list.reverse()
    return task_list
    
    
    pass

# 7. Görev listesinde geçen belirli bir kelimeyi arayıp dönen fonksiyon
def find_task_with_keyword(task_list: list, keyword: str) -> list:
    result=[]

    for task in task_list:
        if keyword.lower() in task.lower():
            result.append(task)
    return result
    
   


    pass

# 8. Görev listesinde en uzun görevi döndür
def get_longest_task(task_list: list) -> str:
    en_uzun_gorev=max(task_list,key=len)
    return en_uzun_gorev
    


    pass

# 9. Görevleri sıralı bir şekilde döndür (alfabetik)
def sort_tasks(task_list: list) -> list:
    task_list.sort()
    return task_list
    pass

# 10. Görev listesindeki toplam karakter sayısını döndür
def total_character_count(task_list: list) -> int:
    toplam_karakter_sayisi=0
    for task in task_list:
        if len(task)>0:
            toplam_karakter_sayisi=toplam_karakter_sayisi+len(task)
    return toplam_karakter_sayisi
    pass