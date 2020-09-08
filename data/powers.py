fx = { # fx from actor to target (includes buffs)

	# fire
	'BLAZE_ATTACK.FX':'blaze',
	'FIREBALL.FX':'blaze',
	'BLAZINGBOLT_ATTACK.FX':'blazing bolt',
	'/INFERNOBOLT.FX':'blazing bolt',
	'FLARES_ATTACK.FX':'flares',
	'INFERNO_ATTACK.FX':'inferno',

	# ice
	'BITTERFREEZERAY.FX':'bib', # misleading name
	'BITTERICEBOLT.FX':'bfr',
	'BITTERFREEZEBOLT.FX':'bfr',
	'ICEBLAST.FX':'ice blast',
	'FREEZERAY.FX':'freeze ray',

	# psi
	'WILLDOMINATION.FX':'will dom',
	'TELEKINETICBLAST.FX':'tk blast',
	'PSIONICLANCEBLASTQUICK.FX':'psi lance',

	# BEAMRIFLE_DISINTEGRATE
	'BEAMRIFLE_DISINTEGRATE.FX':'disintegrate',
	'BEAMRIFLE_CHARGEDSHOT.FX':'penetrating ray/charged shot',
	'BEAMRIFLE_LANCERSHOT.FX':'lancer',
	'BEAMRIFLE_PIERCINGBEAM.FX':'piercing beam',

	# emp
	'HEALINGHANDS.FX':'heal other',
	'ABSORBPAIN.FX':'absorb pain',
	# 'STRENGTHHANDS2.FX':,
	'EMPATHY/RADIATIONEMISSION.FX':'healing aura',
	'MINDWALL.FX':'clear mind',
	'ENDURANCE.FX':'adreneline boost',
	'FORTITUDE.FX':'fortitude',
	'EMPATHYCUREWOUNDS.FX':'regen aura',
	'ADRENALINEFLOW.FX':'recovery aura',

	# pain
	# 'SOOTH_ATTACK.FX':'soothe',
	# 'SHAREPAIN_ATTACK.FX':'share pain',
	'SOOTH_ATTACK.FX':'heal other', # just counting the same as emp for simplicity
	'SHAREPAIN_ATTACK.FX':'absorb pain',
	'PAINBRINGER_ATTACK.FX':'painbringer',

	# psn
	'/POISONLIQUIDPROJECTILE.FX':'envenom',
	'/PALMPOISONLIQUIDPROJECTILE.FX':'weaken',

	# cold
	'HEATLOSSBLAST.FX':'heat loss',

	# rad
	# this is actually the onhit animation as the activation animation EVERVATINGFIELDHANDS doesnt have target info for some reason
	'ENERVATINGFIELDCONTINUING.FX': 'enervating field',

	# ill
	'ILLUSDECOY.FX':'phantom army',
	'ILLUSTERROR.FX':'spectral terror',
	'/ILLUSDECIEVE.FX':'confuse',
	'ILLUSIONCONTROL/ILLUSBLIND.FX':'blind', # attack and target? need to match up w/ MOV MOUTH

	# grav
	'/GCDISTORTION.FX':'gravity distortion',
	'/GCCRUSH_SINGULARITY.FX':'crush',
	'/GCDIMENSIONSHIFT.FX':'dimension shift', # toggle on

	# plant
	# 'THORNS/BUILDUP_ATTACK.FX':'toxins',
	'THORNS/BUILDUP_ATTACK.FX':'build up',
	'PLANTCONTROLHIT.FX':'strangler', # shared with plant control
	# 'STRANGLERROOTS.FX': 'strangler', # doesn't spawn on every strangler

	# elec
	'REJUVENATINGCIRCUITATK.FX':'rejuvenating circuit',
	'EMPOWERINGCIRCUITATK.FX':'empowering circuit',
	'INSULATINGCIRCUITATK.FX':'insulating circuit',
	'AMPUPATTACK.FX':'amp up',
	'/ENERGIZINGCIRCUITATK.FX':'energizing circuit',
	'WITCHESLIGHTNINGBOLTMEGA.FX':'shock',
	'/GALVANICSENTINELSUMMON.FX':'galvanic sentinel',
	# 'ENERGYSINKCASTATTACK.FX':'shock', # galvanic shock

	#nature
	'CORROSIVESAP.FX':'corrosive enzyme',
	'/WILDBASTION.FX':'wild bastion',
	'/OVERGROWTH.FX':'overgrowth',
	'/REGROWTH2.FX':'regrowth',

	# trick arrow
	'/ARROW_NET.FX':'entangling arrow',
	'/ARROW_STICKY.FX':'glue arrow',
	'/ARROW_ACID.FX':'acid arrow',

	# epics
	'/COMMAND2.FX':'dominate',
	'SCHOOLOFSHARKS_HIT.FX':'ssj', # not sure about this one
	'V_MAKO_SPIRITSHARK_CIRCLE_HIT':'ssj',
	# 'SPIRTSHARKJAWS_CONDITIONAL.FX': 'ssj',
	'/HIBERNATE.FX':'hibernate',
	'/HIBERNATE_CONTINUING.FX':'hibernate',
	'/SOOT.FX':'char',
	'/BUILDUPPOWERBOOST.FX':'power boost',
	# '/EMBERSHITSOOTANDCINDERS.FX':'char', # hit?

	# pools
	'JAUNT_ATTACK.FX':'jaunt',
	'SPIRITWARD.FX':'spirit ward',
	'FLIGHT/NONCOMBATFLIGHT':'mystic/flight',
	'MYSTICFLIGHT.FX':'mystic/flight',
	'/INVISPHASE_FASTCAST.FX':'phase shift',
	'PHASESHIFT_ATTACK.FX':'phase shift',
	'MEDICINE/MAID.FX':'aid other', # or aid other
	'AIDOTHER_ATTACK.FX':'aid other', # or aid other
	'/TELEPORT_ATTACK.FX':'translocation', # MOV A_\TRANSLOCATION
	'AIRSUPERIORITY_ATTACK.FX':'air superiority', # 

	# misc powerset
	'FOSSILIZEHANDS.FX':'fossilize',
	'/STALAGMITESTOMP.FX':'stalagmites',

	'/SHIVER.FX':'shiver',
	'/CHILLBLAINSHANDS.FX':'chilblain',

	'/THUNDEROUSBLAST.FX':'thunderous blast',
	'ZAPP_QUICK.FX':'zapp',
	'LIGHTNINGBOLT.FX':'lightning bolt',
	'CHARGEDBOLTS.FX':'charged bolt',

	'/KININERTIALREDUCTIONS.FX':'ir',
	'/KINSIPHONSPEED.FX':'siphon speed',
	'/KINTRANSFERENCE.FX':'transference',

	'/EXECUTIONERSSHOT_ATTACK.FX':'executioner shot',
	'/PIERCINGROUNDS_ATTACK.FX':'piercing rounds',
	'SUPPRESSIVEFIRE_ATTACK.FX':'suppressive fire',

	
	'/WATERJET.FX':'water jet',
	'WATERJET_FAST.FX':'water jet',
	'/DEHYDRATE.FX':'dehydrate',
	
	'POWERPUSH.FX':'power push',
	'ENERGYBLAST/MEGA.FX':'power burst', #?!
	'ENERGYBLAST/SNIPERBLAST_QUICK.FX':'sniper blast', 
	'ENERGYBLAST.FX':'energy blast', 
	
	
	'ASSASINSPSIBLADE.FX':'assassin\'s strike', 
	'PSIBLADEGREAT.FX':'greater psi blade', 

	'/FORCEBOLT.FX':'force bolt',
	'BOOSTRANGE_ATTACK.FX':'boost range', 
	'AIM.FX':'aim',
	'FOLLOWUPHIT4.FX':'build up', #'fiery embrace',
	'/TIDALFORCES.FX':'aim', #water
	'AIM_ACTIVATION.FX':'aim',

	# misc generic
	'ALIGNMENT_JUSTICE.FX':'call to justice',
	# 'WEAPONS/LASER_PISTOL_1.FX':'crey pistol', # using MOV count
	# '/STOLLEN_IMOBILIZER_PISTOL.FX':'crey pistol', #  'stollen'
	'GEASTHEKINDONESCONTINUING.FX':'geas',
	'/ALIGNMENT_FRENZY.FX':'frenzy', # or other insp?
	'/BRAWL_ATTACK.FX':'brawl',

	# insps
	'/STAMINA.FX':'green',
	'/WILLPOWER.FX':'red',
	'/INTELLIGENCE.FX':'blue',
	'/STRENGTH.FX':'purple/orange',
	'/AGILITY.FX':'yellow', # maybe not?

	# temp
	'WEBGRENADETHROW.FX':'web nade',
	'/SKYRAIDERJETS.FX':'raptor pack', # num toggle ons - not time
}


resdebuff = 'DEBUFFDAMRESCONTINUING.FX'

evade = [
	'phase shift',
	'hibernate',
	'jaunt',
	'translocation',
]

healhit = {
	# emp
	'EMPATHY/HEALINGDRAINBALL.FX':'absorb pain',
	'/HEALING.FX':'heal other', # or aid other

	# elec
	'/INSULATINGCIRCUITHIT.FX':'insulating circuit',
	'/REJUVENATINGCIRCUITHIT.FX':'rejuvenating circuit',

	# pools
	'SPIRITWARD_HIT.FX':'spirit ward',
}


pmov = { # prepend with 'A_' for flying version
	'DRAW_PISTOL':'crey pistol',
	'DRAW_WEAPONBACK':'crey pistol', # vill
	'WALL':'ssj',
	'MOUTH':'blind',
	#'PLAYER_HITDEATH' # death anim
}


# primary attacks for determining spike instances (i.e. ignore jaunts off flares or snipe only or w/e)
primaryattacks = [
	'envenom',
	'corrosive enzyme',
	'dominate',
	'blaze',
	'bib',
	'lancer',
	'char', # maybe? depends on lineup
	'penetrating ray/charged shot',
]

utility = [	# for filtering out not atk offense powers
	'shock',
	'entangling arrow',
	'weaken',
	'siphon speed',
	'transference',
	'force bolt',
	'web nade',
	'glue arrow',
	'confuse',
	'brawl',
	'thunderous blast',
	'heat loss',
	'suppressive fire',
]


# generic FX by the actor - usage determined by target's FX
preverse = [
	# buffs
	'ENDURANCE.FX',
	'MINDWALL.FX',
	'FORTITUDE.FX',

	#attacks - note this means misses for these powers don't get counted
	'/PLANTCONTROLHIT.FX',
	'SCHOOLOFSHARKS_HIT.FX',
	'/V_MAKO_SPIRITSHARK_CIRCLE_HIT',

	'ENERVATINGFIELDCONTINUING.FX'
	'/DEHYDRATE.FX',
]


buffs = [
	'HEALINGHANDS.FX',
	'ABSORBPAIN.FX',
	'STRENGTHHANDS2.FX',
	'ENDURANCE.FX',
	'MINDWALL.FX',
	'FORTITUDE.FX',
	'REJUVENATINGCIRCUITATK.FX',
	'EMPOWERINGCIRCUITATK.FX',
	'INSULATINGCIRCUITATK.FX',
	'AMPUPATTACK.FX',
	'PAINBRINGER_ATTACK.FX',
	'WILD_GROWTH_HIT.FX',
	'WILDBASTION_HIT.FX',
	'KINSPEEDBOOSTHIT.FX'
]

gatherbuffs = [
	'WILDBASTION_HIT.FX',
	'KINSPEEDBOOSTHIT.FX',
	'KININERTIALREDUCTIONSCONTINUING.FX',
]

heals = [
	'heal other',
	'absorb pain',
	'rejuvenating circuit',
	'insulating circuit',
	'spirit ward'
]

absorbs = [
	# 'insulating circuit',
	'spirit ward'
]

npc = [
	'NPC',
	'EntTypeFile',
]

# filter out non-player entities - issues if player name = one of these
# probably a better way to do this
name_filter  = [
	'Mu Guardian',
	'Phantasm',
	'Decoy Phantasm',
	'Decoy',
	'Coralax Blue Hybrid',
	'Dr',
	'Poison Trap',
	'Animated Stone',
	'Superior Vigilant Assault',
	'Blind',
	'Galvanic Sentinel',
	'Voltaic Geyser',
	'Voltaic Sentinel',
	'Water Spout',
	'Fortunata Mistress',
	'Superior Scourging Blast',
	'German Shepherd',
	'Ice Storm',
	'Energy Font',
	'Spectral Terror',
	'Coralax Red Hybrid',
	'Faraday Cage',
	'Architect Entertainment Instructor',
	'Architect Contact',
	'Spirit Panther',
	'Ticket Vendor',
	'Architect Entertainment Greeter',
]
