import pandas as pd 

class Base:
    def __init__(self):
        self.df = None
        self.csv_file = r'netflix_list.csv'
        self.get_data()
        self.clean_data()

    def return_string(self):
        return self.csv_file
    
    def get_data(self):
        self.df = pd.read_csv(self.csv_file)
        return self.df
    
    def clean_data(self):

        #removing unnecessary columns which contained nulls
        self.df.drop(columns=['certificate'])

        # filling in any other null factors 
        self.df.fillna(0, inplace = True)
    

if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.df)
    c.df.to_csv('netflix_list_clean.csv')

