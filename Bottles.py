def carton_breakup(bottles):
    carton_sizes = {"xl": 48, "large": 24, "medium": 12, "small": 6}
    
    carton_count = {"xl": 0, "large": 0, "medium": 0, "small": 0}
    
    for carton, size in carton_sizes.items():
        if bottles >= size:
            carton_count[carton] = bottles // size
            bottles %= size
    
    result = []
    for carton, count in carton_count.items():
        if count > 0:
            result.append(f"{count} {carton}")
    
    print(", ".join(result))

carton_breakup(140)