# STRENDA DB

## Administration

## Data

### Publication

This is the publication that includes the experimental results of an enzyme kinetics characterization.

- **title**
  - Type: string
  - Description: title of the publication
- doi
  - Type: string
  - Description: identifier of the publication
- pmid
  - Type: string
  - Description: identifier of the publication as indexed in PubMed
- author
  - Type: Author[]
- experiment
  - Type: Experiment[]

### Author

- **name**
  - Type: string
  - Description: name of the author. Nomenclature: Family name initials first name
- affiliation
  - Type: string
  - Description: name of organizaton, department, city, country
- email
  - Type: string
  - Description: email address
- orcid
  - Type: string
  - Description: ORCID idenfier

### Experiment

- name_of_experiment
  - Type: string
  - Description: name of the experiment, just for internal purposes
- type_of_assay
  - Type: string
  - Description: name of the assay
- direction_of_the_assay
  - Type: string
- definition_of_the_compound_monitored
  - Type: string
  - Description:
- continuously_monitored
  - Type: string
  - Description: selection of the stopping procedure
- directly_monitored
  - Type: string
- protein_assay
  - Type: ProteinDescription

### ProteinDescription

- uniprotkb_ac
  - Type: string
  - Description: identifier obtained from UniProtKB
- protein_name
  - Type: string
  - Description: name of the protein as of UniProtKB
- protein_sequence
  - Type: SequenceModifications
  - Description: amino acid sequence as from UniProtKB
- posttranslational_modifications
  - Type: PosttranslationalModifications
- protein_source
  - Type: ProteinSource
- reaction
  - Type: ProteinReaction
- protein_characterization
  - Type: Dataset[]

### ProteinSource

- expression_system
  - Type: string
  - Description: Description of expression system if heterologously expressed
- organism
  - Type: string
  - Description: as in UniProtKB provided, name of organism
- taxon_id
  - Type: string
  - Description: ID as obtained from NCBI Taxonomy
- strain
  - Type: string
  - Description: name or identifier of the strain
- cell_type
  - Type: string
  - Description: determination of the cell in which the protein is expressed
- tissue
  - Type: string
  - Description: determination of the tissue, ideally BTO is used
- localization
  - Type: string
  - Description: determination of the localization (membran, cytosol, etc.)

### SequenceModifications

- sequence_modification
  - Type: string
  - Description: modified amino acid sequence
- specification_of_the_type_of_modification
  - Type: string
  - Description: Description of the types of modifications

### PosttranslationalModifications

- determination_of_ptm
  - Type: string
  - Description: Phosphorylation, Glycosylation, Acetylation, Hydroxylation, Methylation, Other

### ProteinReaction

- ec_number
  - Type: string
  - Description: EC number obtained from ExplorEnz
- reaction_as_in_explorenz
  - Type: string
  - Description: reaction as described in ExplorEnz
- comment
  - Type: string
  - Description: comment on the protein reaction if not properly described in ExplorEnz

### Dataset

- name
  - Type: string
  - Description: name of the dataset
- assay_conditions
  - Type: AssayConditions[]
- results_set
  - Type: ResultsSet[]
- doi
  - Type: string
  - Description: DOI of the dataset

### AssayConditions

- small_assay_components
  - Type: SmallAssayComponents
  - Description: Description of the compound used in the assay
- macromolecular_components
  - Type: MacromolecularComponents
  - Description: Description of the macromolecular components
- concentration_of_the_assayed_protein
  - Type: string
  - Description: value with unit
- description_of_concentration_measurement
  - Type: string
  - Description: free text field
- ph
  - Type: string
  - Description: value and unit
- pd
  - Type: string
  - Description: value and unit
- temperature
  - Type: string
  - Description: value and unit, K and Celsius

### SmallAssayComponents

- role
  - Type: string
  - Description: role in the assay, i.e. substrate, product, etc.
- initial_concentration_fixed
  - Type: string
  - Description: unit, value
- initial_concentration_varied
  - Type: string
  - Description: concentration range, value, unit
- compound_name
  - Type: string
  - Description: name as obtained from PubChem
- inchi
  - Type: string
  - Description: InChi string
- iupac
  - Type: string
  - Description: IUPAC name
- chebi_id
  - Type: string
  - Description: identifier
- pubchem_cid
  - Type: string
  - Description: identifier

### MacromolecularComponents

- role
  - Type: RoleOfComponent
  - Description: role in the assay, i.e. substrate, product, etc.
- initial_concentration_fixed
  - Type: string
  - Description: unit, value
- initial_concentration_varied
  - Type: string
  - Description: concentration range, value, unit
- classification
  - Type: string
  - Description: protein, carbohydrate, DNA, RNA, etc.
- compound_name
  - Type: string
  - Description: name as obtained from PubChem
- inchi
  - Type: string
  - Description: InChi string
- iupac
  - Type: string
  - Description: IUPAC name
- database_used
  - Type: string
  - Description: name of the database
- identifier
  - Type: string
  - Description: identifier

### RoleOfComponent

- substrate
  - Type: string
  - Description: substrate of chemical reaction
- product
  - Type: string
  - Description: production of chemical reaction
- inhibitor
  - Type: string
  - Description: component that inhibits the chemical reaction
- activator
  - Type: string
  - Description: component that activates/enhances the chemical reaction

### CompoundClassification

- protein
  - Type: string
- carbohydrate
  - Type: string
- dna
  - Type: string
- rna
  - Type: string
- lipid
  - Type: string
- other
  - Type: string

### ResultsSet

- name
  - Type: string
  - Description: Name of the results set
- initial_kinetic_parameters
  - Type: InitialKineticsParameters
  - Description: Km, kcat, V, kcat/Km, V/Km
- activation
  - Type: Activation
- inhibition
  - Type: Inhibition

### InitialKineticsParameters

- km
  - Type: string
  - descriptor: value, SE, unit
- kcat
  - Type: string
  - descriptor: value, SE, unit
- v
  - Type: string
  - descriptor: value, SE, unit
- kcat_over_km
  - Type: string
  - descriptor: value, SE, unit
- v_over_km
  - Type: string
  - descriptor: value, SE, unit

### Activation

- affinity_constant
  - Type: string
  - descriptor: value, SE, unit, true or apparent
- velocity_no_activator
  - Type: string
  - Description: velocity without activator
- velocity_at_max_concentration
  - Type: string
  - Description: velocity at maximum concentration of activator
- saturation
  - Type: string
  - Description: statement whether the concentration was saturating or not
- incluence_no_activator
  - Type: string
  - Description: Influence on MM kinetics. Schema: Value, SE, Unit, true/apparent
- influence_at_maxconcentration
  - Type: string
  - Description: Influence on MM kinetics. Schema: Value, SE, Unit, true/apparent

### Inhibition

- reversibility_yes
  - Type: string
  - Description: inhbition type - competitive, uncompetitive, mixed, kic, SE, Unit, Math function
- reversibility_no
  - Type: string
  - Description: ki, SE, Unit, Comment
