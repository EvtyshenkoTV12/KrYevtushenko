class Person:
    def __init__(self, name, surname, birth_date, sex):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.sex = sex

    def __str__(self):
        return f"Surname: {self.surname} Name: {self.name}\n" \
               f"Birth_date: {self.birth_date} Sex: {self.sex}"

    def edit_name(self, value):
        self.name = value

    def edit_surname(self, value):
        self.surname = value


class Worker(Person):
    def __init__(self, name, surname, birth_date, sex, organization, specialization, position, salary,
                 experience):
        super().__init__(name, surname, birth_date, sex)
        self.organization = organization
        self.specialization = specialization
        self.position = position
        self.salary = salary
        self.experience = experience

    def str(self):
        return f"Surname: {self.surname} Name: {self.name}" \
               f"\nBirth date: {self.birth_date} Sex: {self.sex}\n" \
               f"Organization: {self.organization} Specialization: {self.specialization}" \
               f"\nPosition: {self.position} Salary: {self.salary}$ Experience: {self.experience} years"

    @property
    def salary(self):
        return self.salary

    @property
    def experience(self):
        return self.__experience

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if not value >= 1000:
            raise ValueError()
        self.__salary = value

    @experience.setter
    def experience(self, value):
        if not isinstance(value, int):
            raise TypeError()
        if not value >= 0:
            raise ValueError()
        self.__experience = value


class Organization:

    def __init__(self, name, *args):
        self.name = name
        self.workers = []
        self.__iter = 0
        for worker in args:
            self.add_worker(worker)

    def __iter__(self):
        return self

    def next(self):
        self.iter += 1
        if self.__iter > len(self.__workers):
            self.__iter = 0
            raise StopIteration
        return self.workers[self.__iter-1]

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError()
        if worker in self.workers:
            raise ValueError()
        self.workers.append(worker)

    def __str__(self):
        text = f"Name: {self.name}\n"
        for worker in self.workers:
            text += f"\n{worker}\n"
        return text

    def top_experience(self):
        amount_of_workers = 0
        experienced_workers = []
        for worker in self.workers:
            if worker.experience >= 2:
                amount_of_workers += 1
                experienced_workers.append(worker)
        text = f"Amount of workers above 2 years: {amount_of_workers}\n"
        for worker in experienced_workers:
            text += f"\n{worker}\n"
        return text


worker = Worker("Surname1", "Name1", "23.03.2002", "Man", "Company_name", "Specialization", "Position", 5000, 2)
worker1 = Worker("Surname2", "Name2", "19.02.1997", "Man", "Company_name", "Specialization", "Position", 1000, 0)
worker2 = Worker("Aboba", "Aboba", "23.11.1945", "Woman", "Company_name", "Specialization", "Position", 25000, 1)
organization = Organization("Organization", worker)
organization.add_worker(worker2)
text = organization.top_experience()
print(text)
print(organization)

