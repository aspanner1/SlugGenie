const stringGenEds = [
  "Major",
  "Composition (C)",
  "Cross Cultural Analysis (CC)",
  "Ethnicity and Race (ER)",
  "Interpreting Arts and Media (IM)",
  "Mathematical and Formal Reasoning (MF)",
  "Perspectives (PE)",
  "Practice (PR)",
  "Scientific Inquiry (SI)",
  "Statistical Reasoning (SR)",
  "Textual Analysis (TA)",
];

const GEN_ED_CLASSES = stringGenEds.map((genEd) => {
  return { label: genEd, value: { genEdCategory: genEd } };
});

export default GEN_ED_CLASSES;
