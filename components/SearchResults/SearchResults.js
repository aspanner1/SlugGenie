import styles from "/styles/SearchResults.module.css";
import ClassName from "/components/Class/ClassName";
import ProfessorProfile from "/components/Class/ProfessorProfile";
import ProfessorQualityRating from "/components/Class/QualityRating";
import ProfessorDifficultyRating from "/components/Class/ProfessorDifficulty";

function SearchResults() {
  return (
    <div className={styles.resultsTable}>
      <div className={styles.class}>
        <ProfessorProfile />
        <ClassName />
        <ProfessorQualityRating />
        <ProfessorDifficultyRating />
      </div>
      ;
    </div>
  );
}

export default SearchResults;
