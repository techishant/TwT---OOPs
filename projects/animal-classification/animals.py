print("Animals: The word animal comes from the Latin animalis, meaning 'having breath', 'having soul' or 'living being'. The biological definition includes all members of the kingdom Animalia. In colloquial usage, the term animal is often used to refer only to nonhuman animals")

class Animalia():
    def __init__(self,
                scientific_name, 
                common_names, 
                males, females, 
                lifespan,
                phylum, 
                ani_class, 
                order,
                family,
                genus,
                external_links
                ) -> None:
        
        # Assertions

        assert scientific_name is str, f"scientific_name should be a str"
        assert common_names is list, f"common_names should be a list"
        for name in common_names:
            assert name is str, f"common_names' elements should be a str"
        assert males is str, f"males should be a str"
        assert females is str, f"females should be a str"
        assert lifespan is int, f"lifespan should be a int"
        assert phylum in ['Annelids', 'Arthropods', ], f" should be a String"

        # Declaring
        scientific_name = self.scientific_name
        common_names = self.common_names
        males = self.males
        females = self.females
        lifespan = self.lifespan
        phylum = self.phylum
        ani_class = self.ani_class
        order = self.order
        family = self.family
        genus = self.genus
        external_links = self.external_links

