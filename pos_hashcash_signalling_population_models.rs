// FIRST QUESTION
// Is it better to store populations as:
// - structs in HashMaps? (historically Hard)
// - random iteration over HashSets (might be interesting to compare sets)
//   - https://doc.rust-lang.org/rust-by-example/std/hash/hashset.html?search=
// - structs in Vectors? (also a pain in the ass)
//   - https://doc.rust-lang.org/rust-by-example/custom_types/structs.html
// - Matrixes of Vectors? (historically viable)

// I think I want structs because each person has the
// following parameters:
// - price paid
// - star rating
// - refund/tip

// Then we can estimate the cost of the program
// - return on risk (satisfaction) for the fans
// - refund costs for the artist
// - attack costs for the malicious party

extern crate rand;
use rand::prelude::*;

fn main() {
    
    // Producers
    let psr: f64 = 7.0; // public star rating
    let pp: f64 = 10.0; // public price
    // All People
    let ts = 100; // total size
    // Honest People
    let hs = 80; // honest size
    let hl = 6; // honest low
    let hh = 9; // honest high
    // Malicious People
    let ms = 20; // malicious size
    let ml = 1; // malicous low
    let mh = 4; // malicious high
    
    // creates a population of honest and malicious people
    // stored as i32 in a vector
    fn gen_pop(total_size: i32,
               h_size: i32,
               h_low: i32,
               h_high: i32,
               m_size: i32,
               m_low: i32,
               m_high: i32) -> Vec<f64> {
        
        assert_eq!(total_size, h_size + m_size);
        
        let mut people_vec = Vec::new();
        for i in 0..h_size {
            people_vec.push(thread_rng().gen_range(h_low, h_high));
        }
        for i in 0..m_size {
            people_vec.push(thread_rng().gen_range(m_low, m_high));
        }
        
        let mut f64_people_vec = Vec::new();
        for mut i in people_vec {
            let j = i as f64;
            f64_people_vec.push(j);
        }
        
        f64_people_vec
    }
    let pop = gen_pop(ts, hs, hl, hh, ms, ml, mh);
    println!("pop: {:#?}", pop);

    // function to calculate your peronsal pricing differences
    fn personal_pricing(psr: f64,
                        pp: f64,
                        ysr: f64) -> f64 {
        let my_delta = 0.1_f64 * (psr - ysr); 
        let yp_dif = my_delta * pp;
        yp_dif
    }
    
    // check the personal pricing for every member in the population
    fn personal_pop(f64_vec: Vec<f64>,
                    pop_star_rating: f64,
                    pop_price: f64) -> Vec<f64> {
        
        let mut personal_pricing_vec = Vec::new();
        for i in f64_vec {
            personal_pricing_vec.push(personal_pricing(pop_star_rating, pop_price, i));
        }
        personal_pricing_vec
    }
    let ppp = personal_pop(pop, psr, pp); // population personal pricing
    println!("ppp: {:#?}", ppp)

}
