
# Imports
import random
from pcpartpicker import API

# Variables
api = API()
final_component_dict = {'wireless-network-card': None, 'case-fan': None, 'cpu': None, 'cpu-cooler': None, 'headphones': None, 'motherboard': None, 'monitor': None, 'internal-hard-drive': None, 'external-hard-drive': None, 'ups': None, 'fan-controller': None, 'case': None, 'keyboard': None, 'mouse': None, 'wired-network-card': None, 'sound-card': None, 'video-card': None, 'speakers': None, 'optical-drive': None, 'power-supply': None, 'thermal-paste': None, 'memory': None}

# Chose random part from category
def ChosePart(part):
    
    data = api.retrieve(part)[part]
    
    # Try chose random part
    try:
        random_part = random.choice(data)
    except IndexError:
        return None
    
    return random_part
   
# Main function
def main():
    
    # Set region to fr
    api.set_region("fr")
    
    # For all category
    for part in final_component_dict.keys():
        
        # Edit final dict with a random part with function ChosePart()
        result = ChosePart(part)
        
        if result is None:
            print("Erreur lors du choix de %s." % (part))
        else:
            print("Composent choisit : %s" % (result))
            
        final_component_dict[part] = result
        
    print(final_component_dict)

# Launch code
if __name__ == "__main__":
    main()
    