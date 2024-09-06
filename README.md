# DNA Sequence to Amino Acid Translator

#### Python script that translates DNA sequences into amino acid sequences.

## About this Project

### Description/Motivation
This Python project was a part of the Computational and System Biology Research class. The script translates DNA sequences into corresponding amino acid sequences using a provided codon conversion key. It also generates the reverse complement of the input DNA sequence and translates it as well. The project supports reading multiple reading frames and ensures that the amino acid sequences are extracted between start and stop codons.

### How to Use
To run the script, you need to provide two input files: one containing the DNA sequence and another containing the codon-to-amino-acid mapping.
1. Clone this repository
   ```sh
   git clone https://github.com/nmhumbe/dna-sequence-translator.git
   ```
2. Prepare your input files:
   - **DNA Sequence File:** This should contain the raw DNA sequence in FASTA format (e.g., .txt file).
   - **Codon Key File:** A text file mapping each codon to its respective amino acid.
     
3. Run the script:
   ```sh
   python translation.py dna-sequence.txt codon-table.txt
   ```
<!-- ROADMAP -->

## Roadmap
- [X] Read DNA sequence and codon dictionary from files.
- [X] Translate DNA to amino acid sequences using multiple reading frames.
- [X] Generate the reverse complement and translate.
- [ ] Improve error handling for invalid input files.
- [ ] Add support for RNA sequences.
- [ ] Include visualization of translated sequences.

## Contributing
### Installation
1. Ensure you have Python 3.x installed.
2. Clone the repository:
   ```sh
   git clone https://github.com/nmhumbe/dna-sequence-translator.git
   ```
### Guidelines
Contributions are **welcome!** Feel free to fork the repository and submit a pull request. If you find any issues or have ideas for improvements, please open an issue with the tag "enhancement."

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request
   

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Neha Humbe - nehahumbe@g.ucla.edu

Project Link: https://github.com/nmhumbe/DNATranslation


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [FASTA format](https://en.wikipedia.org/wiki/FASTA_format)
* [README Template](https://github.com/othneildrew/Best-README-Template)
  
