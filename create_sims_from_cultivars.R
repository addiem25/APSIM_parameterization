#install packages (first time only)
pkgs <- c('dplyr', 'tidyr', 'pander', 'reshape2', 'ggplot2',
          'magrittr', 'oz', 'knitr', 'rmarkdown', 'shiny')
pkgs_check <- lapply(pkgs, require, character.only = TRUE)
pkgs_check <- unlist(pkgs_check)
if (length(pkgs[!pkgs_check]) > 0) {
  install.packages(pkgs[!pkgs_check], repos = 'http://cran.csiro.au')
}
install.packages("RAPSIM_0.1.0.4949.tar.gz",type="source",repo=NULL)
install.packages("weatherData")

#load packages (every time you start R)
library(dplyr)
library(tidyr)
library(pander)
library(reshape2)
library(ggplot2)
library(magrittr)
library(oz)
library(knitr)
library(rmarkdown)
library(shiny)
library(RAPSIM)
library(weatherData)

#load in files
#set working directory or change to absolute paths below
setwd("yourdirectoryhere")
#cultivars and parameters
cultivar_params<-read.csv("./sorghum_cultivars_for_sim.csv",head=T)
#template sim
template<-"./TEMPLATE_Sorghum.sim"

#create factors for generating sims
#include date and cultivar
date<-format(as.Date(c("2015-05-19","2016-05-24","2017-05-17")))
cultivar<-as.character(cultivar_params$cultivar)
factors<-list(date=date,cultivar=cultivar)
factors_df<-factors %>% exand.grid(stringsAsFactors=FALSE) %>% tbl_df()

#make sim file(s)
#use generateSIM function
sims<-generateSim(template,factors_df)
#don't know what this does
writeLines(sims[[1]],"temp.sim")
length(sims)
#length should be 54 I think (18 cultivars x 3 years = 54 simulations)

#would be a good idea to make met files here too if possible (weather files)
#but this might be a future edit


#Just realized that the table generateSim acts on is actually a list of cultivars
#which means we still need your code to go from the csv I sent into the sorghum.xml file parameters
#then we can use the genotype list from the csv to make a table 