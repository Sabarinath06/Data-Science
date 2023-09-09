class Univariate():
        def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtype=='O'):
                print("qual")
                qual.append(columnName)
            else:
                print("quan")
                quan.append(columnName)
        return quan,qual  

def Univariate(dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5 rule",
                                   "Lesser","Greater","Min","kurtosis","skew"],columns=quan)
    for columnName in quan:
        descriptive[columnName]["Mean"]=dataset[columnName].mean()
        descriptive[columnName]["Median"]=dataset[columnName].median()
        descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
        descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
        descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
        descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
        descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
        descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
        descriptive[columnName]["1.5 rule"]=1.5*descriptive[columnName]["IQR"]
        descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5 rule"]
        descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5 rule"]
        descriptive[columnName]["Min"]=dataset[columnName].min()
        descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
        descriptive[columnName]["skew"]=dataset[columnName].skew()
        descriptive[columnName]["Variance"]=dataset[columnName].var()
        descriptive[columnName]["Std"]=dataset[columnName].std()
return descriptive   

    def get_pdf_probability(dataset,startrange,endrange):
        from matplotlib import pyplot
        from scipy.stats import norm
        import seaborn as sns
        ax=sns.distplot(dataset,kde=True,kde_kws={'color':'blue'},color='Green')
        pyplot.axvline(startrange,color='Red')
        pyplot.axvline(endrange,color='Red')
        #generate a samaple
        sample=dataset
        #calculate parameters
        sample_mean=sample.mean()
        sample_std=sample.std()
        print('Mean=%.3f,Standard Deviation=%.3f'%(sample_mean,sample_std))
        #define the distribution 
        dist=norm(sample_mean,sample_std)
        #sample probabilities for a range of outcomes 
        values=[value for value in range(startrange,endrange)]
        probabilities=[dist.pdf(value) for value in values]
        prob=sum(probabilities)
        print("The area between range({},{}):{}".format(startrange,endrange,sum(probabilities)))
        return prob
    
def stdNBgraph(dataset):
    #Converted to standard normal distribution
    import seaborn as sns
    mean=dataset.mean()
    std=dataset.std()
    values=[i for i in dataset]
    z_score=[((j-mean)/std) for j in values]
    sns.distplot(z_score,kde=True)
    sum(z_score)/len(z_score)
    #z_score.std()    