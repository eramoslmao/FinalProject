import math

class WorkEstimate:
  def __init__(self, name):
    self.name = name
    self.woodSelect, self.steelSelect, self.laborSelect, self.concreteMaterial, self.laborTime, self.steelAmount, self.woodPlank  = self.inputs()

  def inputs(self):
    """The inputs which will be stored for future use are defined by this function
    """
    #First the dictionaries need to be constructed
    laborType = {'electrician': 22,
                 'plumber': 70,
                 'carpenter': 25,
                 'framer': 18,
                 'general contractor': 50,
                 'project manager': 43,
                 'general labor': 18}
    steelMaterial = {'pipe 12in': 550,
                     'pipe 6in': 600,
                     'w8 beam': 400,
                     'w10 beam': 500,
                     'w14 beam': 700,
                     'rebar #3': 1575,
                     'rebar #4': 1600,
                     'rebar #5': 1675}
    woodMaterial = {'treated lumber': 15,
                    'plywood': 600,
                    '2x4': 400,
                    'flooring': 500,
                    'insulation': 700,
                    'roofing': 1575}
    #I want the dictionaries to be displayed upon intialization
    print(laborType)
    print(steelMaterial)
    print(woodMaterial)

    #Need the time for the project, then convert it into hours for easier calcs
    laborInput = int(input('How long is your project? (in weeks): '))
    laborTime = laborInput * 168

    #Concrete needs area for price calc
    concreteMaterial = input('How much area needs to be covered? (in sq ft): ')

    #The needed variables are what will be outputted for their respective calcs
    woodPlank = input('How many planks of wood are needed?: ')
    woodNeeded = input('What kind of wood do you need? Choose from our selection: ')
    if woodNeeded.lower() not in woodMaterial:
      raise ValueError('Material not found')

    woodSelect = woodMaterial[woodNeeded]

    steelAmount = int(input('How much steel is needed? (per ton): '))
    steelNeeded = input('What kind of steel do you need? Choose from our selection: ')
    if steelNeeded.lower() not in steelMaterial:
      raise ValueError('Material not found')

    steelSelect = steelMaterial[steelNeeded]

    laborNeeded = input('What kind of labor do you need? Choose from our selection: ')
    if laborNeeded.lower() not in laborType:
      raise ValueError('Job not found')

    laborSelect = laborType[laborNeeded]

    return woodSelect, steelSelect, laborSelect, concreteMaterial, laborTime, steelAmount, woodPlank


  def steel_calc(self, material):
    """This function defines the total amount of steel needed from the user
    """
    steelSub = int(self.steelAmount) * material
    laborSteel = 1400

    print('The subtotal cost for steel is ', steelSub)
    print('The cost for installation is estimated to be ', laborSteel)
    print('This brings the total steel cost to ', steelSub + laborSteel)

    return steelSub

  def concrete_calc(self, area):
    """This function calculates the subtotal cost of concrete needed from the user
    """
    concreteSub = area * 77
    laborConcrete = 5 * area
    totalConcrete = concreteSub + laborConcrete


    print('The subtotal cost the concrete needed is ', concreteSub)
    print('The cost for installation is estimated to be ', laborConcrete)
    print('This brings the total concrete cost to ', totalConcrete)

    return concreteSub

  def wood_calc(self, choice):
    """This function defines the total amount of wood needed from the user
    """
    woodSub = int(self.woodPlank) * choice
    #Installation prices are assumed constant
    laborWood = 1400
    totalWood = woodSub + laborWood

    print('The subtotal cost for the wood is ', woodSub)
    print('The cost for installation is estimated to be ', laborWood)
    print('This brings the total wood cost to ', totalWood)

    return woodSub

  def labor_calc(self, labor):
    """This function seperately calculates the cost for a certain type of labor
    needed by the user
    """
    laborSub = labor * self.laborTime
    print('The cost for this kind of labor is ', laborSub)

    return laborSub

  def output(self):
    laborPrice = self.labor_calc(self.laborSelect)
    woodPrice = self.wood_calc(int(self.woodSelect))
    steelPrice = self.steel_calc(int(self.steelSelect))
    concretePrice = self.concrete_calc(int(self.concreteMaterial))
