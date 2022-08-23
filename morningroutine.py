import search_seller

morning_routine = {}
morning_routine['wake up'] = ['exercise', 'brush teeth', 'pack lunch']
morning_routine['exercise'] = ['shower']
morning_routine['shower'] = ['get dressed']
morning_routine['get dressed'] = []
morning_routine['brush teeth'] = ['eat breakfast']
morning_routine['eat breakfast'] = []
morning_routine['pack lunch'] = []

if __name__ == "__main__":
    search_seller(morning_routine)


