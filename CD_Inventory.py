#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# BAnson, 2020-Sep-07, created file based on pseudocode provided by
#   DBiesinger in starter file
# BAnson, 2020-Sep-07, added code for class CD, including docstrings
#   Borrowed pieces of code from Assignment06 and Assignment07 for FileIO and IO functions
#   Rewrote "add data" option to reference CD class properties
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__: returns string of CD data

    """
    # TODid Add Code to the CD class
    # -- Constructor -- #
    def __init__(self, ID, ttl, art):
        # -- Attributes -- #
        self.__ID = ID
        self.__title = ttl
        self.__artist = art
        
    # -- Properties -- #
    @property  
    def ID(self):
        return self.__ID  # Creates private attribute
    
    @ID.setter
    def ID (self, value):
        """Sets value of ID based on user input and checks value type is integer.
    
        Args:
            value (int): user input ID
            
        Returns:
            ID value as integer; or error message 
            
        """
        if type(value) == int:
            self.__ID == value
        else:
            raise Exception('ID needs to be integer')
            
            
    @property
    def title(self):
        return self.__title  # Creates private attribute
    
    @title.setter
    def title(self, value):
        """Sets value of title based on user input and checks value type is string.
    
        Args:
            value: (string) user input title
            
        Returns:
            Title value as string; or error message 
            
        """
        if type(value) == str:
            self.__title = value
        else:
            raise Exception('Title needs to be string')
          
            
    @property
    def artist(self):
        return self.__artist  # Creates private attribute
    
    @artist.setter
    def artist(self, value):
        """Sets value of artist based on user input and checks value type is string.
    
        Args:
            value: (string) user input artist
            
        Returns:
            Artist value as string; or error message 
            
        """
        if type(value) == str:
            self.__artist = value
        else:
            raise Exception('Artist needs to be string')
            
    # -- Methods -- #
    def __str__(self):
        return '{:>2}, {}, {}'.format(self.__ID, self.__title, self.__artist)
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODid Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string) = name of file used to read the data from
            lst_Inventory (list of dict) = 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        lst_Inventory.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            lst_Inventory.append(dicRow)
        objFile.close()
        
    # TODid Add code to process data to a file      
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Writes data from inventory table stored in memory to a text file (or creates empty text file if none exists
        
        Args:
            file_name: name of the file to open and write data to (or create)
            lst_Inventory: (list of dicts) 2D data structure that holds the data during runtime.
        
        Returns:
            Text file containing data of current table in memory
        """
        
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
        objFile.close()
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODid add docstring
    """Handling Input / Output:

    properties:

    methods:
        print_menu: -> Displays menu to user
        menu_choice: -> None
        show_inventory: -> Displays current CD Inventory in memory
        get_data: -> (new CD data)

    """
    # TODid add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\nMenu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # TODid add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice: (string) a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # TODid add code to display the current data on screen
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table

        Args:
            lst_Inventory: (list of dicts) 2D data structure that holds the data during runtime.

        Returns:
            None.
            
        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================')
    
    # TODid add code to get CD data from user  
    @staticmethod
    def get_data():
        """Collects three pieces of data from user: ID, title, and artist
        
        Args:
            None
            
        Returns:
            Tuple containing values corresponding to ID (strID), title (strTitle), and artist (strArtist)
            
        """
        
        strID = input('Enter ID: ').strip()
        intID = int(strID)
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        tplUserData = (intID, strTitle, strArtist)
        return tplUserData


# -- Main Body of Script -- #
# TODid Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
    
# 1. When program starts, read in the currently saved Inventory, or create empty file

try:
    FileIO.load_inventory(strFileName, lstOfCDObjects)
except:
    FileIO.save_inventory(strFileName, lstOfCDObjects)
    

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection 
    # 3.1 process exit first
    if strChoice == 'x':
        choice = input('Are you sure you want to exit? [y/n]: ') # prevent exiting accidentally
        if choice.lower() == 'y':
            break
        else:
            continue


    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        tplNewCd = IO.get_data()
        intID, strTitle, strArtist = tplNewCd
        newCD = CD(intID, strTitle, strArtist)

        # # Review entry
        print('\nYou entered: ', newCD)
        choice = input('Add this data to table? [y/n]: ')
        if choice.lower() == 'y':
            # 3.3.2 Add item to the table
            dicRow = {'ID': newCD.ID, 'Title': newCD.title, 'Artist': newCD.artist}
            print(dicRow)
            lstOfCDObjects.append(dicRow)
            IO.show_inventory(lstOfCDObjects)
        else:
            print('Data not added to table.')
        continue  # start loop back at top.
    
    
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
        
    # 3.5 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects) # function call replaces previous code
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
        


