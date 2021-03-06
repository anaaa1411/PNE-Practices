class Gene(Seq):  #This is a child classs
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases) #When calling super, we call a method defined in my parent class.
        self.name = name  #This declares a new atribute that exists in the child class, but not in the parent class
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

# --- Main program
s1 = Seq("AGTACACTGGT") #s1 wont have an atribute called name
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")