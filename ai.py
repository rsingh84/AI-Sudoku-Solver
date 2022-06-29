from __future__ import print_function
from game import sd_peers, sd_spots, sd_domain_num, init_domains, \
    restrict_domain, SD_DIM, SD_SIZE
import random, copy, sys

class AI:
    def __init__(self):
        pass

    def solve(self, problem):
        domains = init_domains()
        restrict_domain(domains, problem) 

        # TODO: implement backtracking search. 

        assign = {}
        decision_stack=[]
        

        while True:
            assign, domains = self.Propagate(assign,domains)

            if (-1,-1) not in assign:
                if len(assign) >= len(sd_spots): # if all spots have been assigned
                    return domains
                else:
                    assign, num = self.make_decision(assign,domains)
                    old_assign = copy.deepcopy(assign)
                    old_domains = copy.deepcopy(domains)
                    decision_stack.append((old_assign,num,old_domains))
            else:
                if len(decision_stack) == 0: # if the decision stack is empty
                    return None
                else:
                    assign,domains = self.backtrack(decision_stack)


    # TODO: add any supporting function you need

    def Propagate(self, assign, domains):

        while True:


            for i in domains:
                if i not in assign:
                    if len(domains[i]) == 1: # Make assignment if domain becomes singleton
                        assign[i] = domains[i][0]
            
            for j in domains:
                if len(domains[j]) == 0:
                    assign[(-1,-1)] = -1
                    return assign, domains


            for spot in assign:
                if len(domains[spot]) > 1:
                    domains[spot] = [assign[spot]]

            continuePropagate = True

            for i in sd_spots:
                for j in sd_peers[i]: # for every peer in spot i 
                    if len(domains[j]) == 1:
                        if domains[j][0] in domains[i]: # if element of j in domain j is in domain of i
                            domains[i].remove(domains[j][0])
                            continuePropagate = False

            if continuePropagate == True:
                return assign, domains





    def make_decision(self,assign,domains):
        value = None
        spots = []
        min = sys.maxsize

        for s in domains:
            curr = len(domains[s])
            if curr > 1:
                if curr < min:
                    min = curr
                    value = s


        x = domains[value][0]
        assign[value] = x


        return assign, value





    def backtrack(self, decision_stack):
        assign, x, domains = decision_stack.pop()
        temp = assign.pop(x)
        domains[x].remove(temp)
        return assign, domains


    #### The following templates are only useful for the EC part #####

    # EC: parses "problem" into a SAT problem
    # of input form to the program 'picoSAT';
    # returns a string usable as input to picoSAT
    # (do not write to file)
    def sat_encode(self, problem):
        text = ""

        # TODO: write CNF specifications to 'text'

        return text

    # EC: takes as input the dictionary mapping 
    # from variables to T/F assignments solved for by picoSAT;
    # returns a domain dictionary of the same form 
    # as returned by solve()
    def sat_decode(self, assignments):
        # TODO: decode 'assignments' into domains
        
        # TODO: delete this ->
        domains = {}
        for spot in sd_spots:
            domains[spot] = [1]
        return domains
        # <- TODO: delete this
