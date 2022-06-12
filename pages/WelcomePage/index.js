import styles from "/styles/WelcomePage.module.css";
import Link from "next/link";
import Card from "/pages/WelcomePage/Card";
import Image from "next/image";
import Panda from "/public/panda.png";

function WelcomePage() {
  return (
    <>
      <Card className={styles.card}>
        <Image
          src={Panda}
          width={100}
          height={100}
          layout="fixed"
          alt="A cute panda waving"
        />
        <h1 className={styles.title}>Planda</h1>
        <Link href="/ClassSearch">
          <button className={styles.button1}>Find Classes</button>
        </Link>
      </Card>
    </>
  );
}

export default WelcomePage;
