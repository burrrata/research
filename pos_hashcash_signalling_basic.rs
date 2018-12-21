/*
 X is your self assessed star rating 
 
 if people feel like the show/thing was less than X give 
 them a refund proportional to the amount less
 
 if people feel like it was greater than X they have an option to tip 
 you (because in reality you provided more than they gave so 
 they kind of "owe" you). 
*/

fn main() {
    
    // Artist Defined Metrics
    let public_star_rating: f64 = 7.0;
    let public_price: f64 = 10.0;
    
    // User Defined Metrics
    let my_star_rating: f64 = 8.0;

    fn personal_pricing(public_star_rating: f64,
                        public_price: f64,
                        my_star_rating: f64) -> f64 {
                            
        let my_delta = 0.1_f64 * (public_star_rating - my_star_rating); // multiply by 0.1 to make the delta a %
        let personal_price_difference = my_delta * public_price;
        
        personal_price_difference
    }
    
    let my_price = personal_pricing(public_star_rating,
                                    public_price,
                                    my_star_rating);
    
    // Print Results
    if my_price < 0.0 {
        println!("We're so glad you enjoyed the show! If you thought that it was worth more than you paid, please consider making a donation of {:?}. Thanks!", -my_price);
    } else if my_price > 0.0 {
        println!("We're sorry you did not enjoy the show. Please accept this refund of {:?} to show our sincere apologies.", my_price);
    } else {
        println!("We hope you enjoyed the show! :)")
    }
    
}
