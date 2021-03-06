from montepython.likelihood_class import Likelihood


class Planck_SZ(Likelihood):

    # initialization routine
    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)

        self.need_cosmo_arguments(data, {'output': 'mPk'})

    # compute likelihood
    def loglkl(self, cosmo, data):

        lkl = -0.5 * pow(((cosmo.sigma8() * pow(cosmo.Omega_m()/self.Omega_m_ref,self.Omega_m_index) - self.bestfit)/self.sigma),2)

        return lkl
