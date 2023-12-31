# STRENDA-DB Specifications

STRENDA stands for "Standards for Reporting Enzymology Data".

STRENDA DB is a storage and search platform supported by the Beilstein-Institut that incorporates the STRENDA Guidelines in a user-friendly, web-based system. If you are an author who is preparing a manuscript containing functional enzymology data, STRENDA DB provides you the means to ensure that your data sets are complete and valid before you submit them as part of a publication to a journal.

The STRENDA Commission, comprising an international panel of highly-regarded scientists who have wide-ranging expertise in areas such as biochemistry, enzyme nomenclature, bioinformatics, systems biology, modelling, mechanistic enzymology and theoretical biology, has established standards for data reporting in enzymology research. The aim of these STRENDA Guidelines is to improve the quality of data published in the scientific literature and to enable researchers to compare, evaluate, interpret and reproduce experimental research results published in the literature and databases. A description of the Guidelines is available here.

## Root

### Dataset

- manuscript
  - Type: Manuscript
  - Description: Manuscript details
- experiments
  - Type: Experiment
  - Description: Experiments that are part of this Dataset
  - Multiple: True
- results
  - Type: Result
  - Description: Results of this dataset
  - Multiple: True

## General information

### Manuscript

- author_names
  - Type: Author
  - Description: Names of the authors (last name, first name)
  - Multiple: True
- DOI
  - Type: string, integer
  - Description: Digital Object Identifier of the given manuscript
- PMID
  - Type: string, integer
  - Description: PubMed identifier of the manuscript

### Author

- first_name
  - Type: string
  - Description: First name of the author
- last_name
  - Type: string
  - Description: Last name of the author

## Experiment Details

The following objects describe the experiment of interest.

### Experiment

- methodology
  - Type: string
  - Description: Free text describing the methodology of the experiment
- proteins
  - Type: Protein
  - Description: Proteins that have been used within this assay
  - Multiple: True
- assay_conditions
  - Type: AssayConditions
  - Description: Conditions of the assay

### Protein

- protein_id
  - Type: string, integer
  - Description: Unique identifier of the given protein
- name
  - Type: string
  - Description: The name of the protein
- sequence
  - Type: string
  - Description: Amino acid of the protein's primary structure
- ec_number
  - Type: string
  - Description: EC number of the protein e.g. '3.4.11.4'
- reaction
  - Type: string
  - Description: Catalyzed reaction of the given protein (from the EC number)
- assayed_reaction
  - Type: string
  - Description: Reaction that the proteins catalyzes within this manuscript

### AssayConditions

- assay_components
  - Type: string
  - Description: Components of this assay
  - Multiple: True
- compound_name
  - Type: string
  - Description: Name of the compound that has been used within this assay
- inchi
  - Type: string
  - Description: International Chemical Identifier of the compound
- iupac_name
  - Type: string
  - Description: IUPAC name of the compound
- database_id
  - Type: string
  - Description: Unique identifier of the database this compound can be found
- concentration
  - Type: PositiveFloat
  - Description: Initial concentration of the given compound
- protein_concentration
  - Type: PositiveFloat
  - Description: Initial concentration of the protein used in this assay
- ph
  - Type: float
  - Description: pH value of the assay
  - gt: 0.0
  - lt: 14.0
- role
  - Type: CompoundRoles
  - Description: Role of this compound. Find the list if roles [here](#compoundroles).

## Results

The following objects descibe the results drawn from the experiment, such as kinetic parameters and inhibition details.

### Result

- kinetic_parameters
  - Type: KineticParameters
  - Description: Estimated kinetic parameters
- inhibition_parameters
  - Type: InhibitionParameters
  - Description: Estimated inhibition parameters
- activation_parameters
  - Type: ActivationParameters
  - Description: Estimated activation parameters

### KineticParameters

- Km
  - Type: float
  - Description: Estimated Michaelis-Menten constant
- kcat
  - Type: float
  - Description: Estimated catalytic rate
- V
  - type: float
  - Description: Reaction velocity
- kcat_over_km
  - Type: float
  - Description: Ratio of the catalytic rate over Michaelis-Menten constant
- V_over_km
  - Type: float
  - Description: Ration of reaction velocity over Michaelis-Menten constant

### InhibitionParameters

- reversible
  - Type: boolean
  - Description: Whether or not this reaction is reversible
- inhibition_type
  - Type: InhibitionType
  - Description: Type of inhibition that occured within this reaction
- Kic
  - Type: float
  - Description: Inhibition constant of the reaction (Case: (un-)competivtive, mixed)
- Kiu
  - Type: float
  - Description: Second inhibition constant of the reaction (Case: mixed)
- Ki
  - Type: float
  - Description: Inhibition constant of the reaction (Case: irreversible reaction)

### ActivationParameters

- activation_affinity_constant
  - Type: float
  - Description: Activation affinity constant of the reaction
- velocity_at_no_activator
  - Type: float
  - Description: Velocity of the reaction at zero concentration of the activator
- velocity_at_max_activator
  - Type: float
  - Description: Velocity of the reaction at maximum concentration of the activator

## Enumerations

### CompoundRoles

```python
SUBSTRATE = "substrate"
PRODUCT = "product"
SALT = "salt"
BUFFER = "buffer"
INHIBITOR = "inhibitor"
ACTIVATOR = "activator"
```

### InhibitionType

```python
COMPETITIVE = "competitive"
UNCOMPETITIVE = "uncompetitive"
MIXED = "mixed"
```
